# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `CrackToss_71`
- **Input XML**: `outputs/batch/CrackToss/CrackToss/CrackToss_71/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/CrackToss.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 32 |
| Player Tracks | 32 |
| Ball Tracks | 0 |
| CSV events parsed | 18 |
| Action Segments inferred | 80 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 249 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 249 as fallback play end.
> - Action 'Action_None' range [107-128] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-135] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-218] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [221-241] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [246-249] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-231] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [107-175] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-181] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-196] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-249] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [107-121] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-178] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-206] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [159-221] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [107-226] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-235] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-176] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-238] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-171] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-119] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-197] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [206-208] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-137] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-164] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-249] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-236] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-128] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-140] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-144] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-152] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-149] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-241] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-216] for track '25' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [205-238] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [223-231] for track '30' has 1 frames without a visible bounding box.
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