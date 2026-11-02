# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `JetSweep_49`
- **Input XML**: `outputs/batch/JetSweep/JetSweep/JetSweep_49/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/JetSweep.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 44 |
| Player Tracks | 44 |
| Ball Tracks | 0 |
| CSV events parsed | 20 |
| Action Segments inferred | 114 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 389 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 100: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
> - Row 100: Duplicate assignment for track ID '8' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
> - Resolved action overlap for track '11' (C): higher_priority='Action_BallSnap' [72–83], lower_priority='Action_ZoneBlock' annotated_start=74, effective_Action_ZoneBlock_start=84.
> - Action 'Action_None' range [72-107] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-135] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [74-103] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [125-148] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [74-122] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-133] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_SealBlock' range [74-208] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_SealBlock' range [231-238] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_LeadBlock' range [74-113] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [74-97] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [105-106] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-126] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-199] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [210-307] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [101-134] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-87] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [89-94] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-114] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-131] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [84-85] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [88-92] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [95-124] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-154] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [184-361] for track '11' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [72-190] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-75] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-109] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-120] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-125] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-128] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-80] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-259] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [268-284] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-5] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_JetMotion' range [67-98] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [101-193] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [208-239] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [256-257] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [260-263] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [281-282] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [286-287] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [289-293] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [298-299] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [309-310] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-143] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [208-356] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [361-375] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [380-389] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [126-138] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-135] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-178] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-281] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-169] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-238] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-229] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [249-250] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-208] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [215-237] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-299] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-240] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [210-222] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [226-307] for track '27' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [312-313] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [346-380] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [382-389] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [219-242] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [254-285] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [295-301] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [303-306] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [222-282] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [230-389] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [233-247] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [251-259] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [243-384] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [273-349] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [294-296] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [335-339] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [342-347] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [349-354] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [356-357] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [363-372] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [362-369] for track '42' has 2 frames without a visible bounding box.
> - Player track '0' has undefined position. Will map to Position_Unknown.
> - Player track '0' has undefined team_side. Will map to Team_Unknown.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.