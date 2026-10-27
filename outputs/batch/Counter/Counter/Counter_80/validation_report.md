# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_80`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_80/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 44 |
| Player Tracks | 44 |
| Ball Tracks | 0 |
| CSV events parsed | 18 |
| Action Segments inferred | 115 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 329 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
> - Overlapping action conflict at frame 62 for track '12': 'Action_BallSnap' vs 'Action_DownBlock'. Overriding with 'Action_DownBlock'.
> - Action 'Action_None' range [62-101] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-119] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-213] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-82] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-124] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-91] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-74] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-98] for track '3' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [62-156] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [232-237] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [247-269] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-134] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-300] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [62-99] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-205] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [239-264] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-100] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [104-148] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-85] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-197] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [62-89] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [99-125] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [133-140] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-172] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-179] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-190] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-135] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-171] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-179] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-210] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_SnapReceive' range [62-69] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [101-146] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [65-77] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [86-89] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [95-121] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [123-124] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-290] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-80] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-192] for track '13' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [81-85] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-93] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-100] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-123] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-210] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [246-250] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-107] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-122] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-179] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-263] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-163] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-199] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-186] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [208-212] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [225-306] for track '21' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [120-174] for track '22' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [180-185] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-140] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-150] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-171] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-177] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-187] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-203] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [207-236] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [239-247] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [253-329] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-169] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-175] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-207] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-164] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [172-216] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [162-181] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-206] for track '27' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [163-196] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-179] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-218] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [239-277] for track '29' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [191-196] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-287] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-203] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-251] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [254-279] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [286-321] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-201] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-263] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [274-295] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-213] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [215-227] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [233-258] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [235-286] for track '38' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [243-253] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [248-266] for track '40' has 6 frames without a visible bounding box.
> - Action 'Action_None' range [298-301] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [304-329] for track '43' has 2 frames without a visible bounding box.
> - Player track '13' has undefined position. Will map to Position_Unknown.
> - Player track '13' has undefined team_side. Will map to Team_Unknown.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
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