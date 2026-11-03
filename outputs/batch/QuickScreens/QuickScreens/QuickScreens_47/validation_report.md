# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `QuickScreens_47`
- **Input XML**: `outputs/batch/QuickScreens/QuickScreens/QuickScreens_47/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/QuickScreens.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 47 |
| Player Tracks | 47 |
| Ball Tracks | 0 |
| CSV events parsed | 18 |
| Action Segments inferred | 163 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 329 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Action 'Action_PreSnap' range [0-176] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [182-185] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-48] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [51-220] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [226-227] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [230-246] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-9] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-29] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_ScreenBlock' range [10-46] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_ScreenBlock' range [63-66] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [84-112] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-115] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-323] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-189] for track '4' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [198-204] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [207-282] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-8] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-17] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [19-29] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_RunAfterCatch' range [63-64] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_RunAfterCatch' range [66-70] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_RunAfterCatch' range [73-174] for track '6' has 4 frames without a visible bounding box.
> - Action 'Action_RunAfterCatch' range [176-179] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_RunAfterCatch' range [181-329] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-48] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [50-51] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [66-248] for track '7' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-130] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-68] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-58] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [64-159] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-8] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-31] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-51] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [130-169] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [171-175] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [180-184] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-105] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [109-111] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [114-115] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-8] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-17] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [19-30] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-30] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-9] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-17] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-29] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [41-46] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [50-55] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [62-109] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [113-154] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [156-175] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [177-218] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [220-251] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-329] for track '17' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-292] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' for track '19' starts at frame 9, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [9-9] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [11-17] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_ThrowScreenPass' range [22-29] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-3] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [5-8] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [66-67] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [73-218] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [224-225] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [227-234] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [238-239] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [243-245] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [249-251] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-8] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [15-61] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [72-138] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [158-159] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [163-164] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-29] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [56-58] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [66-67] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [73-112] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [114-116] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [128-148] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [152-159] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [162-164] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [172-173] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [56-140] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [146-148] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [152-182] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [187-189] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [198-201] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [204-213] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [218-253] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [256-307] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [62-140] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [152-153] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [158-162] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [169-182] for track '25' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [185-329] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [73-83] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [74-138] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [158-159] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [196-199] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [206-210] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [213-258] for track '27' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [265-267] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [74-109] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [127-138] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [74-246] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [248-254] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [257-310] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [82-100] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [103-111] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [127-130] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [132-138] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [87-90] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [111-165] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [172-177] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [201-211] for track '31' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [213-218] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [220-246] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [133-136] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [159-160] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [174-180] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [184-189] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [196-215] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [217-218] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [220-233] for track '34' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [235-236] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [243-248] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [191-195] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [196-201] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [215-217] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [228-229] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [231-304] for track '36' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [209-211] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [253-258] for track '37' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [214-254] for track '38' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [257-258] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [260-303] for track '38' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [230-234] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [239-241] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [252-253] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [257-258] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [260-321] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [232-282] for track '40' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [236-246] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [248-251] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [253-304] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [255-268] for track '42' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [257-290] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [258-319] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [266-267] for track '45' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [305-306] for track '46' has 1 frames without a visible bounding box.
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