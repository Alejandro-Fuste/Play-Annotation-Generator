# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_363`
- **Input XML**: `outputs/batch/Power/Power/Power_363/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 28 |
| Player Tracks | 28 |
| Ball Tracks | 0 |
| CSV events parsed | 15 |
| Action Segments inferred | 52 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 449 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 449 as fallback play end.
> - Action 'Action_PreSnap' range [20-437] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-422] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [425-428] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-332] for track '2' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-449] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-442] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-420] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-418] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-363] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-441] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-74] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [77-426] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [428-435] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-391] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-385] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [392-419] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-312] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [314-323] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [332-335] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-318] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [320-323] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [327-443] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [446-449] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-449] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [28-310] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [311-323] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [331-443] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [337-342] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [344-346] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [344-350] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [352-368] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [372-375] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [360-363] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [376-449] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [436-448] for track '27' has 1 frames without a visible bounding box.
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