# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_45`
- **Input XML**: `outputs/batch/Power/Power/Power_45/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 35 |
| Player Tracks | 35 |
| Ball Tracks | 0 |
| CSV events parsed | 14 |
| Action Segments inferred | 57 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Action 'Action_PreSnap' range [5-163] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [5-269] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [5-195] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [197-221] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [252-264] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [5-269] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [5-230] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [232-233] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [236-242] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [245-250] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [5-269] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [5-269] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [5-201] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [203-252] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [260-262] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [5-269] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [126-149] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [152-181] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-201] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-205] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [126-153] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [5-250] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [5-135] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [143-159] for track '16' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [5-137] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [5-269] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [5-269] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [5-11] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-125] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [126-152] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [130-131] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [165-166] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [169-238] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [183-184] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [207-216] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [219-220] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [222-224] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [237-238] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [247-249] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [237-247] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [258-262] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [259-267] for track '34' has 1 frames without a visible bounding box.
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
> - Player track '32' has undefined position. Will map to Position_Unknown.
> - Player track '32' has undefined team_side. Will map to Team_Unknown.
> - Player track '33' has undefined position. Will map to Position_Unknown.
> - Player track '33' has undefined team_side. Will map to Team_Unknown.
> - Player track '34' has undefined position. Will map to Position_Unknown.
> - Player track '34' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.