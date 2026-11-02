# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `JetSweep_86`
- **Input XML**: `outputs/batch/JetSweep/JetSweep/JetSweep_86/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/JetSweep.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 38 |
| Player Tracks | 38 |
| Ball Tracks | 0 |
| CSV events parsed | 24 |
| Action Segments inferred | 139 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 329 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
> - Resolved action overlap for track '20' (C): higher_priority='Action_BallSnap' [83–95], lower_priority='Action_ZoneBlock' annotated_start=89, effective_Action_ZoneBlock_start=96.
> - Action 'Action_None' range [83-154] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-161] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [173-179] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-188] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [83-210] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [113-164] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [169-173] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [175-261] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [265-297] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [308-311] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [83-145] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-156] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [83-175] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-329] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-153] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-164] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [168-239] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [83-231] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [237-238] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [240-242] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [256-257] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [83-134] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-137] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-268] for track '7' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [83-329] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [83-289] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [292-329] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-120] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-230] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [89-114] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [121-145] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-166] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [169-252] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [83-158] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-175] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-286] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_SealBlock' range [89-136] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_SealBlock' range [145-164] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_SealBlock' range [168-267] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_SealBlock' range [274-284] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_SealBlock' range [292-293] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [83-118] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [83-196] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [83-112] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-134] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-138] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [83-174] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [89-94] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [89-102] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [104-134] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [136-141] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-179] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-227] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [236-237] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [239-249] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [105-110] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-223] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [233-247] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [257-258] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [263-265] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [273-274] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [279-288] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [295-300] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [302-310] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-91] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-133] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-259] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-153] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-269] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [271-272] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [274-329] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [145-251] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [257-325] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-178] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-215] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [217-221] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [223-228] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [235-245] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-175] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-187] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-190] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-203] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [184-268] for track '26' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [271-275] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [277-279] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-256] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [259-260] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [263-294] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [296-321] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [326-328] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [223-262] for track '28' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [270-279] for track '28' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [281-287] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [249-251] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [250-317] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [293-310] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [294-298] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [295-297] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [300-302] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [315-316] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [320-325] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [322-325] for track '36' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.