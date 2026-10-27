# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_374`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_374/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 38 |
| Player Tracks | 37 |
| Ball Tracks | 1 |
| CSV events parsed | 19 |
| Action Segments inferred | 79 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Resolved action overlap for track '14' (C): higher_priority='Action_BallSnap' [85–90], lower_priority='Action_DownBlock' annotated_start=88, effective_Action_DownBlock_start=91.
> - Action 'Action_PullBlock' range [88-174] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [175-204] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [85-171] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-176] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-247] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [85-151] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [85-213] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [85-167] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-173] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [177-178] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [85-188] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [88-135] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-226] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [85-174] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [136-139] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [85-168] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-211] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [85-200] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-202] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [85-194] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [88-174] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-215] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-113] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-174] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-106] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-110] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-231] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-156] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-145] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-174] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [161-167] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-175] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-183] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [184-220] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-226] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [231-232] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [235-236] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [241-245] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [253-255] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [232-248] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [251-257] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [233-234] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [236-244] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [248-249] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [258-261] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [265-266] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [262-265] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [268-269] for track '36' has 1 frames without a visible bounding box.
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
> - Player track '35' has undefined position. Will map to Position_Unknown.
> - Player track '35' has undefined team_side. Will map to Team_Unknown.
> - Player track '36' has undefined position. Will map to Position_Unknown.
> - Player track '36' has undefined team_side. Will map to Team_Unknown.
> - Player track '37' has undefined position. Will map to Position_Unknown.
> - Player track '37' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.