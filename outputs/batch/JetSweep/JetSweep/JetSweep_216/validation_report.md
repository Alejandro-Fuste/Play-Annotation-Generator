# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `JetSweep_216`
- **Input XML**: `outputs/batch/JetSweep/JetSweep/JetSweep_216/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/JetSweep.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 30 |
| Player Tracks | 30 |
| Ball Tracks | 0 |
| CSV events parsed | 21 |
| Action Segments inferred | 70 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Resolved action overlap for track '11' (C): higher_priority='Action_BallSnap' [46–57], lower_priority='Action_ZoneBlock' annotated_start=47, effective_Action_ZoneBlock_start=58.
> - Action 'Action_ZoneBlock' range [47-63] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [65-107] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [47-95] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [99-113] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [46-269] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [46-246] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [250-269] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-93] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-110] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [47-98] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-116] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-124] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_LeadBlock' range [47-87] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-116] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [119-120] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-269] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [58-110] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [47-114] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-61] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-57] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-77] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-106] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-111] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-233] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-134] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-140] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-176] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [71-73] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [75-195] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [198-215] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-98] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-112] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-105] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_JetMotion' range [98-99] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-165] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [128-238] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-186] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [195-196] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [210-212] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [235-240] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [243-244] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [247-255] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [235-236] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [248-269] for track '29' has 3 frames without a visible bounding box.
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
> - Player track '29' has undefined position. Will map to Position_Unknown.
> - Player track '29' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.