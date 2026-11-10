# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `RPO_220`
- **Input XML**: `outputs/batch/RPO/RPO/RPO_220/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/RPO.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 28 |
| Player Tracks | 27 |
| Ball Tracks | 1 |
| CSV events parsed | 17 |
| Action Segments inferred | 76 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Action 'Action_None' range [63-107] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [109-144] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [63-117] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-267] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [64-103] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [105-106] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [113-117] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [120-121] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-135] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-251] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [124-249] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-142] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-258] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [124-253] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [63-248] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-212] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [63-114] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [116-128] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-140] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [63-64] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-248] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [63-237] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-59] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-114] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-126] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-132] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-55] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [63-64] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [66-252] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [70-73] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-117] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-241] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [133-155] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-147] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-164] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [162-258] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [247-248] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [250-251] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [249-254] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [256-263] for track '27' has 2 frames without a visible bounding box.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
> - Player track '16' has undefined position. Will map to Position_Unknown.
> - Player track '16' has undefined team_side. Will map to Team_Unknown.
> - Player track '18' has undefined position. Will map to Position_Unknown.
> - Player track '18' has undefined team_side. Will map to Team_Unknown.
> - Player track '19' has undefined position. Will map to Position_Unknown.
> - Player track '19' has undefined team_side. Will map to Team_Unknown.
> - Player track '20' has undefined position. Will map to Position_Unknown.
> - Player track '20' has undefined team_side. Will map to Team_Unknown.
> - Player track '21' has undefined position. Will map to Position_Unknown.
> - Player track '21' has undefined team_side. Will map to Team_Unknown.
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