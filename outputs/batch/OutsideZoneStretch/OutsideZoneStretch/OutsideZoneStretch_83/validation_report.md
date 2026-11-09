# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OutsideZoneStretch_83`
- **Input XML**: `outputs/batch/OutsideZoneStretch/OutsideZoneStretch/OutsideZoneStretch_83/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OutsideZoneStretch.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 35 |
| Player Tracks | 35 |
| Ball Tracks | 0 |
| CSV events parsed | 11 |
| Action Segments inferred | 171 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Segment 'Action_ZoneBlock' for track '3' has invalid range: start=149, end=127. Clamping end to start.
> - Action 'Action_PreSnap' range [0-227] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-144] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [146-157] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [171-172] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [177-178] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [197-218] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [221-245] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [247-248] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [250-251] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [254-267] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-149] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [151-165] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [167-187] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-35] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [126-127] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-13] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [34-56] for track '4' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [61-63] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [65-95] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [98-101] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [104-123] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [126-139] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [152-171] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [196-281] for track '4' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-29] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [48-49] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [52-77] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [127-129] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [132-137] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [141-145] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [165-166] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-144] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [202-203] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [206-214] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [218-243] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-17] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-27] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [29-170] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [185-218] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-25] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [30-45] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [72-116] for track '8' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [132-133] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [138-140] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [146-150] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-187] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [189-227] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-1] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [24-25] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [28-34] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [40-41] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [73-74] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [76-77] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [82-127] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [132-133] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [162-163] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [171-175] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [2-3] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [16-18] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-46] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [67-71] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [78-88] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [90-99] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [142-144] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PressEdge' for track '10' starts at frame 161, but the player has no visible bounding box on this frame.
> - Action 'Action_PressEdge' range [161-161] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PressEdge' range [163-180] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PressEdge' range [182-187] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PressEdge' range [191-192] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [203-206] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [211-212] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [241-242] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [10-14] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [65-67] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [70-72] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [74-78] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [82-85] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [112-122] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [125-127] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [129-136] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [139-140] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [153-154] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [158-166] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [184-196] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [217-218] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [229-286] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [294-296] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [30-56] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [60-62] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [67-69] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [78-135] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [75-136] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [139-145] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [147-148] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [152-153] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [157-163] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [166-190] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [210-230] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [239-282] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [284-294] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [80-90] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [106-111] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [137-138] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [146-147] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [150-153] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [160-162] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [165-166] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [171-194] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [222-226] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [105-119] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [127-130] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [133-139] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [143-146] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [152-160] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [166-168] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [171-179] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [182-185] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [192-204] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [209-213] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [227-239] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [243-252] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [133-145] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [149-153] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [157-223] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [235-244] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [258-259] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [147-153] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [159-167] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [169-206] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [159-177] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [187-197] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [203-208] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [211-299] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [168-170] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [172-177] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [200-201] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [173-183] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [174-179] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [181-183] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [189-229] for track '21' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [232-235] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [237-238] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [174-181] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [187-191] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [193-211] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [186-235] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [188-201] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [210-213] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [194-230] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [210-276] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [278-286] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [290-291] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [211-235] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [238-242] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [245-250] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [228-271] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [231-262] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [232-248] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [262-265] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [296-299] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [281-286] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [288-292] for track '33' has 1 frames without a visible bounding box.
> - Player track '10' has undefined position. Will map to Position_Unknown.
> - Player track '10' has undefined team_side. Will map to Team_Unknown.
> - Player track '11' has undefined position. Will map to Position_Unknown.
> - Player track '11' has undefined team_side. Will map to Team_Unknown.
> - Player track '12' has undefined position. Will map to Position_Unknown.
> - Player track '12' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.