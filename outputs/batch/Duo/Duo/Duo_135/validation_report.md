# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Duo_135`
- **Input XML**: `outputs/batch/Duo/Duo/Duo_135/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Duo.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 32 |
| Player Tracks | 32 |
| Ball Tracks | 0 |
| CSV events parsed | 17 |
| Action Segments inferred | 54 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 268 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 268 as fallback play end.
> - Deduplicated duplicate event 'Action_ComboBlock' at frame 136 for track '15'.
> - Action 'Action_PreSnap' range [0-148] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [156-232] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-189] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [192-199] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [203-210] for track '4' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [226-227] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-239] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-163] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [175-185] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-260] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [263-268] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-268] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-160] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-161] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [174-268] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [136-147] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [149-150] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-244] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-255] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [136-177] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-206] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [233-238] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-194] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-266] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-196] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-133] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [170-171] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [184-268] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [160-164] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [187-189] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [191-257] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [193-194] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [203-268] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [215-218] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [222-223] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [226-230] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [237-238] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [255-257] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [263-268] for track '31' has 1 frames without a visible bounding box.
> - Player track '22' has undefined position. Will map to Position_Unknown.
> - Player track '22' has undefined team_side. Will map to Team_Unknown.
> - Player track '23' has undefined position. Will map to Position_Unknown.
> - Player track '23' has undefined team_side. Will map to Team_Unknown.
> - Player track '24' has undefined position. Will map to Position_Unknown.
> - Player track '24' has undefined team_side. Will map to Team_Unknown.
> - Player track '25' has undefined position. Will map to Position_Unknown.
> - Player track '25' has undefined team_side. Will map to Team_Unknown.
> - Player track '26' has undefined position. Will map to Position_Unknown.
> - Player track '26' has undefined team_side. Will map to Team_Unknown.
> - Player track '27' has undefined position. Will map to Position_Unknown.
> - Player track '27' has undefined team_side. Will map to Team_Unknown.
> - Player track '28' has undefined position. Will map to Position_Unknown.
> - Player track '28' has undefined team_side. Will map to Team_Unknown.
> - Player track '29' has undefined position. Will map to Position_Unknown.
> - Player track '29' has undefined team_side. Will map to Team_Unknown.
> - Player track '30' has undefined position. Will map to Position_Unknown.
> - Player track '30' has undefined team_side. Will map to Team_Unknown.
> - Player track '31' has undefined position. Will map to Position_Unknown.
> - Player track '31' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.