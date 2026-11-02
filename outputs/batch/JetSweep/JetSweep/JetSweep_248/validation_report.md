# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `JetSweep_248`
- **Input XML**: `outputs/batch/JetSweep/JetSweep/JetSweep_248/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/JetSweep.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 37 |
| Player Tracks | 37 |
| Ball Tracks | 0 |
| CSV events parsed | 21 |
| Action Segments inferred | 119 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Overlapping action conflict at frame 87 for track '0': 'Action_ZoneBlock' vs 'Action_LeadBlock'. Overriding with 'Action_LeadBlock'.
> - Resolved action overlap for track '11' (C): higher_priority='Action_BallSnap' [86–98], lower_priority='Action_ZoneBlock' annotated_start=87, effective_Action_ZoneBlock_start=99.
> - Action 'Action_LeadBlock' range [87-158] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [86-238] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [254-299] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-146] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [86-141] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [144-148] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-196] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [86-96] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-235] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [237-242] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [248-249] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [86-97] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [86-147] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-155] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [86-103] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-107] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-171] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [176-177] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [86-102] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-194] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-199] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-299] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [163-183] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-194] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-201] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [86-184] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-192] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-227] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [86-117] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [12-17] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-109] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [121-156] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-187] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-191] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-210] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [113-210] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [212-224] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [226-232] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [240-242] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [87-132] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-93] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-120] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-129] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-137] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [213-214] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-299] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-150] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-182] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-199] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-214] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [216-280] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [132-137] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-144] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [158-160] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-180] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [182-185] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [189-223] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [231-232] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [234-245] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-139] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [162-166] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-187] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-196] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-164] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-168] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-173] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-182] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-175] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-252] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [255-298] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-230] for track '28' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [177-252] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [262-268] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [285-299] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-251] for track '30' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [254-299] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-215] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [217-234] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [234-249] for track '33' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [251-256] for track '33' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [258-273] for track '33' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [280-295] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [251-254] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [255-258] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [260-265] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [273-274] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [280-281] for track '36' has 1 frames without a visible bounding box.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '33' has undefined position. Will map to Position_Unknown.
> - Player track '33' has undefined team_side. Will map to Team_Unknown.
> - Player track '34' has undefined position. Will map to Position_Unknown.
> - Player track '34' has undefined team_side. Will map to Team_Unknown.
> - Player track '35' has undefined position. Will map to Position_Unknown.
> - Player track '35' has undefined team_side. Will map to Team_Unknown.
> - Player track '36' has undefined position. Will map to Position_Unknown.
> - Player track '36' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.