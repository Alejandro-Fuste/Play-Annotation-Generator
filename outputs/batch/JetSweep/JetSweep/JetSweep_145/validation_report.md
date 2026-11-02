# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `JetSweep_145`
- **Input XML**: `outputs/batch/JetSweep/JetSweep/JetSweep_145/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/JetSweep.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 42 |
| Player Tracks | 41 |
| Ball Tracks | 1 |
| CSV events parsed | 24 |
| Action Segments inferred | 219 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 291: Duplicate assignment for track ID '17' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Validation warning: Action 'Action_LeadBlock' for track '0' (RB) duration 95 frames exceeds threshold 90 frames [start=55, end=149].
> - Resolved action overlap for track '14' (C): higher_priority='Action_BallSnap' [53–68], lower_priority='Action_ZoneBlock' annotated_start=55, effective_Action_ZoneBlock_start=69.
> - Validation warning: Action 'Action_ZoneBlock' for track '19' (RT) duration 95 frames exceeds threshold 90 frames [start=55, end=149].
> - Validation warning: Action 'Action_ZoneBlock' for track '20' (LT) duration 95 frames exceeds threshold 90 frames [start=55, end=149].
> - Segment 'Action_ZoneBlock' for track '21' has invalid range: start=55, end=35. Clamping end to start.
> - Action 'Action_None' range [150-166] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [168-169] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [53-98] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [106-109] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-129] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-150] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-269] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [53-136] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [138-139] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-143] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-147] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [53-106] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-117] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-129] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-138] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-147] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-158] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-200] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [212-219] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [223-224] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [53-181] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-196] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [210-224] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [232-245] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [252-253] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [258-259] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [53-56] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [59-64] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [66-70] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-115] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-130] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-150] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [152-158] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [162-164] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-196] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [201-202] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-227] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [53-98] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-108] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [53-85] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-92] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-98] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-109] for track '8' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [111-115] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [127-138] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [53-70] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [53-56] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [59-64] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [66-72] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-85] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-98] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [53-56] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [59-68] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [53-56] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [59-60] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [66-70] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [79-80] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-98] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-108] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [53-56] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [59-68] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [69-71] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [79-82] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_JetMotion' range [33-70] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_JetMotion' range [79-80] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [84-136] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [155-158] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [165-166] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [171-177] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [181-183] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [53-60] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [63-64] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [66-68] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [79-87] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-98] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-108] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-127] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [55-56] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [59-62] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [66-71] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [79-80] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [53-56] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [66-70] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [79-91] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-98] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-136] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-54] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [55-56] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [66-68] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [79-118] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [128-129] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-173] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-185] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-193] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [223-224] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [230-235] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [55-71] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [78-85] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [91-98] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [105-140] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [143-147] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [150-159] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [170-177] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [179-207] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [209-210] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [28-35] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [69-72] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [79-98] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [102-103] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-122] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-81] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [83-85] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-98] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-108] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-132] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-136] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-158] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [165-166] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-269] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [83-90] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [94-98] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-153] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-158] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-166] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-185] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [84-85] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-118] for track '26' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [120-197] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-221] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [223-227] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [232-235] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-109] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-118] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-122] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-129] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-129] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-150] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-166] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-175] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-185] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-196] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-200] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-269] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-132] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-185] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-194] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [198-269] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-136] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-158] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [161-166] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-188] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [190-198] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [210-225] for track '31' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [227-228] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-158] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-158] for track '33' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [161-178] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-186] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-191] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-202] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-218] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-182] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-191] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [212-219] for track '35' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [233-234] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-200] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-206] for track '36' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [214-219] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [231-235] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [237-242] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [244-269] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [208-221] for track '37' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [223-269] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [212-224] for track '38' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [233-235] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [213-219] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [226-227] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [233-235] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [240-246] for track '40' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.