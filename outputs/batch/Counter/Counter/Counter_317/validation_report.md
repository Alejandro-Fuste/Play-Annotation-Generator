# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_317`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_317/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 47 |
| Player Tracks | 47 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 160 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 359 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 636: Duplicate assignment for track ID '12' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
> - Validation warning: Action 'Action_PullBlock' for track '12' (RG) duration 103 frames exceeds threshold 90 frames [start=85, end=187].
> - Validation warning: Action 'Action_DownBlock' for track '18' (LG) duration 103 frames exceeds threshold 90 frames [start=85, end=187].
> - Validation warning: Action 'Action_DownBlock' for track '20' (C) duration 103 frames exceeds threshold 90 frames [start=85, end=187].
> - Resolved action overlap for track '20' (C): higher_priority='Action_BallSnap' [82–97], lower_priority='Action_DownBlock' annotated_start=85, effective_Action_DownBlock_start=98.
> - Action 'Action_None' range [82-232] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [234-236] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [239-243] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-204] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [215-359] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-126] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-136] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [82-263] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [265-267] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-180] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-189] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-208] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-113] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-128] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-131] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-159] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [162-164] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-139] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-351] for track '10' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [82-118] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-143] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [145-147] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-156] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-162] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-359] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [85-159] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [164-179] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-189] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-201] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-208] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [82-182] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-122] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [133-261] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [264-359] for track '14' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [82-190] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-263] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [267-320] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [322-342] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-109] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-359] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [85-102] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [109-111] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [118-121] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [125-128] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [131-133] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [138-154] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [157-166] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [172-173] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [183-184] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [234-235] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [237-258] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [268-270] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [85-104] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [98-128] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [130-131] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [141-187] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-191] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-272] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [277-292] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [85-159] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [162-164] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [167-168] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-204] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [206-216] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [218-219] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [227-237] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [112-113] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-119] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-126] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-353] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-133] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-148] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-173] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [158-162] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-169] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [171-175] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-195] for track '28' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [198-230] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [232-263] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-351] for track '29' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [204-205] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [218-262] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [264-274] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [277-359] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-270] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [277-280] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [292-359] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [220-221] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [223-224] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [233-250] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [255-294] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [297-304] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [307-353] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [253-255] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [256-259] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [265-269] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [269-353] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [272-277] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [282-303] for track '38' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [308-310] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [315-325] for track '38' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [340-341] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [344-347] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [287-291] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [319-320] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [289-290] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [294-295] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [297-300] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [305-324] for track '40' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [326-329] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [334-337] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [342-343] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [308-310] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [312-359] for track '41' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [312-317] for track '42' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [316-359] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [331-333] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [342-348] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [354-359] for track '44' has 3 frames without a visible bounding box.
> - Player track '1' has undefined position. Will map to Position_Unknown.
> - Player track '1' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '46' has undefined position. Will map to Position_Unknown.
> - Player track '46' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.