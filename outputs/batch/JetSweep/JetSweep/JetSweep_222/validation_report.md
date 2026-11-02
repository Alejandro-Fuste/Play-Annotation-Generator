# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `JetSweep_222`
- **Input XML**: `outputs/batch/JetSweep/JetSweep/JetSweep_222/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/JetSweep.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 40 |
| Player Tracks | 40 |
| Ball Tracks | 0 |
| CSV events parsed | 23 |
| Action Segments inferred | 105 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 446: Duplicate assignment for track ID '15' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Segment 'Action_BallCarry' for track '19' has invalid range: start=87, end=84. Clamping end to start.
> - Action 'Action_None' range [118-128] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-194] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-102] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-172] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [58-105] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-164] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-210] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_LeadBlock' range [59-70] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_LeadBlock' range [79-85] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [59-116] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-153] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-154] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-163] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-79] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-166] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-172] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [59-117] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-153] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-210] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-116] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-154] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-161] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-137] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-145] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-150] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-210] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [58-115] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-150] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [58-76] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-72] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-164] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [58-135] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-69] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-100] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-119] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-157] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-153] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-172] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-68] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-82] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-110] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-130] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [133-134] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-153] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-174] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_JetMotion' range [66-80] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_JetMotion' range [82-84] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [67-102] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-118] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [120-122] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-171] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-153] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-161] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-133] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-153] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-198] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [203-210] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [162-190] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [163-166] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-210] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-170] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [195-210] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-184] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-210] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-210] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-174] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-186] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-210] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-209] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-186] for track '34' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [189-198] for track '34' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [178-180] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-186] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-210] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-182] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-183] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-205] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-199] for track '39' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [206-208] for track '39' has 1 frames without a visible bounding box.
> - Player track '12' has undefined position. Will map to Position_Unknown.
> - Player track '12' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.