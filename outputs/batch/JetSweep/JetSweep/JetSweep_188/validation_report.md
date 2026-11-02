# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `JetSweep_188`
- **Input XML**: `outputs/batch/JetSweep/JetSweep/JetSweep_188/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/JetSweep.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 42 |
| Player Tracks | 42 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 115 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Validation warning: Action 'Action_LeadBlock' for track '1' (TE1) duration 93 frames exceeds threshold 90 frames [start=54, end=146].
> - Validation warning: Action 'Action_ZoneBlock' for track '12' (LG) duration 93 frames exceeds threshold 90 frames [start=54, end=146].
> - Validation warning: Action 'Action_ZoneBlock' for track '14' (LT) duration 93 frames exceeds threshold 90 frames [start=54, end=146].
> - Segment 'Action_BallSnap' for track '20' has invalid range: start=63, end=61. Clamping end to start.
> - Action 'Action_ZoneBlock' range [54-85] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_LeadBlock' range [54-87] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_LeadBlock' range [90-106] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-194] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [201-213] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [53-71] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [53-90] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [53-199] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-260] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [262-263] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [53-106] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-139] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [53-200] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_JetMotion' range [37-81] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [94-102] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [113-153] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [53-81] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [53-104] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-109] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-165] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-269] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [53-54] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-124] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-129] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [54-94] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [54-81] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [86-100] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [102-146] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [228-269] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-122] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-164] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-187] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-194] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [53-65] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-104] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [106-108] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-147] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-172] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [53-70] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-73] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-83] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [53-68] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-79] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [83-150] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [53-65] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [79-204] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [53-98] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-106] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-83] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [89-92] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-142] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-172] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-179] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-92] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-104] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-100] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-117] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-156] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-131] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-135] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-129] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-146] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-209] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [215-216] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [218-269] for track '28' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [136-164] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-169] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-178] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [181-183] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-269] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [136-140] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-166] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-239] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-153] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-157] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-262] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-203] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [216-224] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [232-235] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [243-256] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [258-261] for track '41' has 1 frames without a visible bounding box.
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
> - Player track '38' has undefined position. Will map to Position_Unknown.
> - Player track '38' has undefined team_side. Will map to Team_Unknown.
> - Player track '39' has undefined position. Will map to Position_Unknown.
> - Player track '39' has undefined team_side. Will map to Team_Unknown.
> - Player track '40' has undefined position. Will map to Position_Unknown.
> - Player track '40' has undefined team_side. Will map to Team_Unknown.
> - Player track '41' has undefined position. Will map to Position_Unknown.
> - Player track '41' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.