# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `RPO_114`
- **Input XML**: `outputs/batch/RPO/RPO/RPO_114/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/RPO.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 28 |
| Player Tracks | 28 |
| Ball Tracks | 0 |
| CSV events parsed | 16 |
| Action Segments inferred | 63 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Action 'Action_None' range [121-132] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [63-119] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [121-217] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PullBall' range [86-90] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-135] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [63-222] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-239] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-266] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [63-149] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-190] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [195-233] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [63-159] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-255] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [63-221] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-146] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-183] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-269] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-134] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-235] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-256] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-138] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-255] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [257-258] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-182] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [220-260] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [220-253] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [248-249] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [257-258] for track '27' has 1 frames without a visible bounding box.
> - Player track '13' has undefined position. Will map to Position_Unknown.
> - Player track '13' has undefined team_side. Will map to Team_Unknown.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
> - Player track '16' has undefined position. Will map to Position_Unknown.
> - Player track '16' has undefined team_side. Will map to Team_Unknown.
> - Player track '17' has undefined position. Will map to Position_Unknown.
> - Player track '17' has undefined team_side. Will map to Team_Unknown.
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