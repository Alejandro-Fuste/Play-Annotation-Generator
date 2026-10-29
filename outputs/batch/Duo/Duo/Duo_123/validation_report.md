# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Duo_123`
- **Input XML**: `outputs/batch/Duo/Duo/Duo_123/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Duo.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 28 |
| Player Tracks | 28 |
| Ball Tracks | 0 |
| CSV events parsed | 17 |
| Action Segments inferred | 59 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [0-239] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-239] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-239] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-239] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-239] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [122-166] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [169-171] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-220] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-239] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-186] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [190-191] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [193-200] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [204-210] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [215-239] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-214] for track '9' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [227-230] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-239] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-239] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-168] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [172-173] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [193-196] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-199] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [203-204] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [210-239] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-179] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [184-239] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-186] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [189-227] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [235-239] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-194] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [201-202] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-164] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [167-168] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [176-177] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-157] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [191-193] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-185] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [188-203] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [205-239] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-223] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [225-239] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-212] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [216-218] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [222-239] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [32-33] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [209-239] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [211-221] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [223-239] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [223-226] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [231-239] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [231-234] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [234-237] for track '27' has 2 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.