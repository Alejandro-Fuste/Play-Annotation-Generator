# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `JetSweep_132`
- **Input XML**: `outputs/batch/JetSweep/JetSweep/JetSweep_132/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/JetSweep.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 33 |
| Player Tracks | 33 |
| Ball Tracks | 0 |
| CSV events parsed | 23 |
| Action Segments inferred | 91 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Resolved action overlap for track '12' (C): higher_priority='Action_BallSnap' [74–87], lower_priority='Action_ZoneBlock' annotated_start=75, effective_Action_ZoneBlock_start=88.
> - Segment 'Action_ZoneBlock' for track '13' has invalid range: start=75, end=67. Clamping end to start.
> - Action 'Action_PreSnap' range [0-33] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-269] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-132] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [75-91] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [102-104] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [109-111] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [113-117] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [127-131] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [74-158] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [74-165] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [74-135] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-152] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-225] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_SealBlock' range [75-95] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_SealBlock' range [101-111] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_SealBlock' range [136-141] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_Toss' range [91-101] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-145] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-130] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [75-134] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-143] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-136] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [74-80] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-138] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-163] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-166] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-20] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-44] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [55-67] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [74-75] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [83-121] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-141] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-28] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-136] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [138-150] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-80] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [83-160] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_JetMotion' range [63-87] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_JetMotion' range [89-98] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [103-106] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [108-123] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [127-170] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [173-229] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [231-239] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [74-108] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [81-135] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_LeadBlock' range [88-123] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [141-245] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-120] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-231] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [125-131] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [139-141] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-182] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-226] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [236-255] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [257-269] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-164] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-173] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-188] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-252] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [262-269] for track '31' has 1 frames without a visible bounding box.
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
> - Player track '30' has undefined position. Will map to Position_Unknown.
> - Player track '30' has undefined team_side. Will map to Team_Unknown.
> - Player track '31' has undefined position. Will map to Position_Unknown.
> - Player track '31' has undefined team_side. Will map to Team_Unknown.
> - Player track '32' has undefined position. Will map to Position_Unknown.
> - Player track '32' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.