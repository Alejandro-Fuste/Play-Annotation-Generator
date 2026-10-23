# TapeVision Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `JetSweep_3`
- **Input XML**: `outputs/batch_test_5/JetSweep/JetSweep_3/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/JetSweep.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 46 |
| Player Tracks | 46 |
| Ball Tracks | 0 |
| CSV events parsed | 29 |
| Action Segments inferred | 159 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Resolved action overlap for track '15' (C): higher_priority='Action_BallSnap' [40–55], lower_priority='Action_ZoneBlock' annotated_start=41, effective_Action_ZoneBlock_start=56.
> - Action 'Action_None' range [40-282] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-55] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [61-62] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [40-96] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [101-143] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-183] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [41-127] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-266] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [270-299] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [71-247] for track '4' has 3 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [249-285] for track '4' has 3 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [288-292] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [297-298] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [40-299] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [40-233] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [240-242] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [40-89] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-96] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-210] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [220-299] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [40-109] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [40-61] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-96] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [99-100] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [40-74] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [76-85] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [89-91] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-129] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_LeadBlock' range [41-127] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [128-245] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [40-275] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [41-127] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [128-280] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [282-299] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [40-54] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-227] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [231-251] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [253-285] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [40-192] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [194-195] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [40-119] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-122] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-299] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [41-54] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-229] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [231-243] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [245-253] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [256-276] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [278-284] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [288-298] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-251] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [256-257] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [40-292] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [294-296] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [298-299] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-100] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-111] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-122] for track '23' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [125-265] for track '23' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [268-273] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [275-299] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-126] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [146-155] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-181] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-191] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-129] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-185] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-240] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-207] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-233] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [235-250] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [259-266] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [269-285] for track '29' has 6 frames without a visible bounding box.
> - Action 'Action_None' range [288-290] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [292-295] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-207] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [208-209] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [220-221] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [245-247] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [230-233] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [235-238] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [243-244] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [241-245] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [243-256] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [262-266] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [293-295] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [246-247] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [250-251] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [253-255] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [266-269] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [272-273] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [289-292] for track '36' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [251-256] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [267-272] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [282-291] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [274-277] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [282-285] for track '39' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [287-292] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [295-296] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [275-276] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [279-280] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [284-285] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [290-291] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [294-298] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [282-285] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [289-292] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [290-296] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [295-296] for track '44' has 1 frames without a visible bounding box.
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
> - Player track '42' has undefined position. Will map to Position_Unknown.
> - Player track '42' has undefined team_side. Will map to Team_Unknown.
> - Player track '43' has undefined position. Will map to Position_Unknown.
> - Player track '43' has undefined team_side. Will map to Team_Unknown.
> - Player track '44' has undefined position. Will map to Position_Unknown.
> - Player track '44' has undefined team_side. Will map to Team_Unknown.
> - Player track '45' has undefined position. Will map to Position_Unknown.
> - Player track '45' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.