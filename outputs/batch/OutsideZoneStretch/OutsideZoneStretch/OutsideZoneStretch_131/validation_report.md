# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OutsideZoneStretch_131`
- **Input XML**: `outputs/batch/OutsideZoneStretch/OutsideZoneStretch/OutsideZoneStretch_131/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OutsideZoneStretch.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 42 |
| Player Tracks | 42 |
| Ball Tracks | 0 |
| CSV events parsed | 19 |
| Action Segments inferred | 154 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Segment 'Action_ZoneBlock' for track '7' has invalid range: start=186, end=53. Clamping end to start.
> - Segment 'Action_ZoneBlock' for track '13' has invalid range: start=186, end=70. Clamping end to start.
> - Action 'Action_PreSnap' range [0-176] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [186-277] for track '0' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [279-299] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-144] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [147-186] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [191-206] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [209-220] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [223-241] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [243-253] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [259-262] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [267-269] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [274-277] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [279-280] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-91] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [97-144] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [146-153] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [158-159] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [161-165] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-299] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-299] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-42] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [44-46] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [49-55] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [58-64] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [70-112] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [118-158] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [165-185] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [186-212] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [214-215] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [229-232] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [236-238] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [248-255] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [259-260] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [262-263] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [296-298] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-186] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-53] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-154] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [159-163] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [167-225] for track '8' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [232-238] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [240-241] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [253-258] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [260-289] for track '8' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [295-296] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-154] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-158] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-70] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-94] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-51] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [53-70] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-293] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [295-297] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PressEdge' range [29-58] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PressEdge' range [63-66] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-283] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [286-296] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-148] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [150-178] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [182-299] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-63] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [66-73] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [76-77] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [83-90] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [93-118] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [120-135] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [143-147] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [149-153] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [156-159] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [165-181] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [186-188] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [196-198] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [203-204] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [247-248] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [262-263] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [265-267] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [281-284] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-28] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [100-121] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [126-132] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [134-153] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [186-233] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [234-268] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [270-297] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-182] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [184-190] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [193-194] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [196-199] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [203-206] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [210-215] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [229-233] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [240-246] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [248-250] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [258-299] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [64-69] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [67-73] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [77-163] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [75-80] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [104-158] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [163-168] for track '24' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [170-176] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [185-194] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [196-223] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [233-234] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [237-238] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [240-276] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [282-283] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [290-296] for track '24' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [78-160] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [163-164] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [166-199] for track '25' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [203-214] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [81-82] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [98-126] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [114-115] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [169-181] for track '29' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [184-186] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [174-194] for track '30' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [197-203] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [205-210] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [210-212] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [214-229] for track '32' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [233-259] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [261-270] for track '32' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [272-279] for track '32' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [284-287] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [296-299] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [211-217] for track '33' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [219-262] for track '33' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [212-214] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [241-244] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [255-258] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [245-246] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [248-252] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [255-260] for track '37' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [262-284] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [286-299] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [271-273] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [294-296] for track '39' has 1 frames without a visible bounding box.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
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
> - Metadata: no Dataset Summary row found for output_file 'OutsideZoneStretch_131'; source metadata written as null.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.