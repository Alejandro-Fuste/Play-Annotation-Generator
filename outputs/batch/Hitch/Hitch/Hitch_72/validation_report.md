# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Hitch_72`
- **Input XML**: `outputs/batch/Hitch/Hitch/Hitch_72/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Hitch.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 46 |
| Player Tracks | 46 |
| Ball Tracks | 0 |
| CSV events parsed | 20 |
| Action Segments inferred | 159 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 81: Duplicate assignment for track ID '17' in grid. Overwriting previous assignment.
> - Row 82: Duplicate assignment for track ID '1' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Resolved action overlap for track '20' (C): higher_priority='Action_BallSnap' [26–38], lower_priority='Action_PassBlock' annotated_start=28, effective_Action_PassBlock_start=39.
> - Action 'Action_None' range [26-237] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-94] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-127] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-240] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [242-269] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-78] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-108] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-87] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-90] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-138] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-187] for track '6' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [189-198] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-89] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-94] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-238] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [240-242] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-59] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [61-63] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-76] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-269] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-123] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-132] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-118] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-132] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-160] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [162-168] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-175] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [184-187] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-190] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-207] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [210-211] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [215-220] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [238-240] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [245-246] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-43] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-19] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [28-90] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [28-153] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [159-162] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [165-167] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [173-175] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [194-195] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [203-227] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [39-69] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-107] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-152] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [157-162] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [173-176] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-184] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-44] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [26-28] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [39-40] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [42-49] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [54-269] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-11] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [28-33] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [37-38] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [41-44] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-114] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-198] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-217] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [247-269] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [75-112] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [122-123] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-129] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-133] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-161] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-167] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-174] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-183] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [186-201] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-205] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [226-227] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [229-266] for track '24' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [268-269] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [93-111] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-137] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [151-178] for track '25' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [180-191] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-200] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [210-212] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [226-228] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [230-235] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [245-247] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [253-260] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [264-265] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [267-269] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-200] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-213] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-227] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [232-233] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [235-237] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [243-247] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [253-269] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-227] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [139-150] for track '29' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [161-248] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [140-153] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [158-210] for track '30' has 4 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [212-269] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-191] for track '31' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [194-210] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [212-221] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [223-224] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-148] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-151] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-161] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-269] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-162] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-177] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-191] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-194] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-201] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [195-200] for track '37' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [195-209] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [211-213] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [223-229] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [237-240] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [231-240] for track '40' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [246-247] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [249-250] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [244-247] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [256-269] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [258-260] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [264-268] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [258-260] for track '45' has 1 frames without a visible bounding box.
> - Player track '19' has undefined position. Will map to Position_Unknown.
> - Player track '19' has undefined team_side. Will map to Team_Unknown.
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