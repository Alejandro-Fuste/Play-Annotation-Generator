# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_183`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_183/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 26 |
| Player Tracks | 26 |
| Ball Tracks | 0 |
| CSV events parsed | 18 |
| Action Segments inferred | 81 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Action 'Action_None' range [140-209] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [213-219] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [140-283] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [286-287] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [289-299] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-237] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [248-299] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-290] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-159] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [162-176] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-160] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [162-199] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [203-204] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-225] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [227-299] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [145-185] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [140-206] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [210-212] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [218-225] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [229-299] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [140-290] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-204] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [211-212] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [10-170] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [180-239] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [241-242] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-205] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [145-207] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [140-204] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [208-216] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [145-173] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [145-209] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [214-215] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-188] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-204] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-212] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [214-215] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [226-235] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [237-299] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [232-299] for track '25' has 2 frames without a visible bounding box.
> - Player track '0' has undefined position. Will map to Position_Unknown.
> - Player track '0' has undefined team_side. Will map to Team_Unknown.
> - Player track '5' has undefined position. Will map to Position_Unknown.
> - Player track '5' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.