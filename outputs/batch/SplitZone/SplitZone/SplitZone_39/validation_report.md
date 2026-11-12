# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `SplitZone_39`
- **Input XML**: `outputs/batch/SplitZone/SplitZone/SplitZone_39/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/SplitZone.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 38 |
| Player Tracks | 38 |
| Ball Tracks | 0 |
| CSV events parsed | 23 |
| Action Segments inferred | 141 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 329 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
> - Validation warning: Action 'Action_ZoneBlock' for track '16' (C) duration 113 frames exceeds threshold 90 frames [start=120, end=232].
> - Resolved action overlap for track '16' (C): higher_priority='Action_BallSnap' [117–128], lower_priority='Action_ZoneBlock' annotated_start=120, effective_Action_ZoneBlock_start=129.
> - Validation warning: Action 'Action_ZoneBlock' for track '18' (RT) duration 113 frames exceeds threshold 90 frames [start=120, end=232].
> - Validation warning: Action 'Action_ZoneBlock' for track '20' (LT) duration 113 frames exceeds threshold 90 frames [start=120, end=232].
> - Validation warning: Action 'Action_ZoneBlock' for track '21' (LG) duration 101 frames exceeds threshold 90 frames [start=120, end=220].
> - Action 'Action_None' range [117-190] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-198] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [203-206] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-243] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [250-251] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-308] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [310-317] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [117-212] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [215-303] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [305-324] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [159-298] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [303-310] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [117-314] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [316-326] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-7] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [43-48] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-130] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-138] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-151] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-156] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-180] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-269] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [14-15] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-24] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-32] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [64-88] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [94-95] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [97-99] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-138] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [140-141] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [197-329] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [37-46] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-159] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [162-163] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-215] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [222-225] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [46-59] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [62-100] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [102-107] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [109-113] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-164] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [179-180] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-201] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [234-275] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [52-116] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [117-126] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [132-144] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [147-157] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [163-183] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [205-206] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [211-212] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [233-312] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [319-325] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [62-123] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [120-159] for track '18' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [233-272] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [120-123] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [127-128] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [140-157] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [161-172] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [180-181] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [120-131] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [136-152] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [233-246] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [120-141] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [148-220] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [67-116] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-128] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-198] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-203] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [107-108] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-122] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-223] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [230-329] for track '25' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [184-185] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-198] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [243-244] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [263-264] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [269-281] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [283-284] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-191] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-208] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [212-221] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [229-232] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [238-239] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [241-287] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [289-312] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-225] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [238-244] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [247-258] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [275-277] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [253-323] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [274-329] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [288-312] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [293-294] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [296-304] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [306-308] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [313-314] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [327-328] for track '37' has 1 frames without a visible bounding box.
> - Player track '11' has undefined position. Will map to Position_Unknown.
> - Player track '11' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.