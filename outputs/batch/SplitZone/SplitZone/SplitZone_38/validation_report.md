# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `SplitZone_38`
- **Input XML**: `outputs/batch/SplitZone/SplitZone/SplitZone_38/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/SplitZone.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 29 |
| Player Tracks | 29 |
| Ball Tracks | 0 |
| CSV events parsed | 21 |
| Action Segments inferred | 91 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Validation warning: Action 'Action_ZoneBlock' for track '4' (RG) duration 96 frames exceeds threshold 90 frames [start=104, end=199].
> - Validation warning: Action 'Action_ZoneBlock' for track '7' (RT) duration 96 frames exceeds threshold 90 frames [start=104, end=199].
> - Validation warning: Action 'Action_ZoneBlock' for track '15' (C) duration 96 frames exceeds threshold 90 frames [start=104, end=199].
> - Resolved action overlap for track '15' (C): higher_priority='Action_BallSnap' [101–111], lower_priority='Action_ZoneBlock' annotated_start=104, effective_Action_ZoneBlock_start=112.
> - Action 'Action_None' range [101-188] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-235] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [239-280] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_SplitBlock' range [107-168] for track '2' has 3 frames without a visible bounding box.
> - Action 'Action_SplitBlock' range [175-191] for track '2' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [200-202] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-273] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [101-153] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-186] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-218] for track '3' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [221-222] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-238] for track '3' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [248-251] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [257-258] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [104-145] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [104-118] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [123-149] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [101-135] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-142] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-182] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [185-188] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [195-196] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-207] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-252] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [259-299] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [104-156] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [101-147] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [208-214] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [101-121] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-299] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [149-207] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [101-125] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-219] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [104-115] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [101-112] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [101-106] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-209] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [220-228] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [149-216] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [123-136] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [162-202] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [206-211] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [220-222] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-274] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [278-279] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-216] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [219-227] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [240-297] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [254-255] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [256-261] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [263-265] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [257-278] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [286-291] for track '27' has 2 frames without a visible bounding box.
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
> - Player track '28' has undefined position. Will map to Position_Unknown.
> - Player track '28' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.