# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_323`
- **Input XML**: `outputs/batch/Power/Power/Power_323/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 38 |
| Player Tracks | 38 |
| Ball Tracks | 0 |
| CSV events parsed | 10 |
| Action Segments inferred | 194 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 646: Duplicate assignment for track ID '8' in grid. Overwriting previous assignment.
> - Row 646: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
> - Row 646: Duplicate assignment for track ID '4' in grid. Overwriting previous assignment.
> - Row 646: Duplicate assignment for track ID '13' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Action 'Action_PreSnap' range [13-22] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-109] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [124-133] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [136-141] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [149-158] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [160-163] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [167-168] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [173-175] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [177-194] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [201-202] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [216-217] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [226-232] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [234-236] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [240-241] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [274-276] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [281-289] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [292-297] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-148] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [152-161] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-255] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [258-259] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [264-265] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-181] for track '3' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-144] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [148-161] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [191-214] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [229-232] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [234-253] for track '4' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-118] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [126-130] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [150-158] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [161-163] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [171-211] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [223-224] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [230-237] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-25] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [30-298] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-252] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [258-263] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [269-270] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-22] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-109] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [112-117] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [126-133] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [148-158] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [160-163] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [173-176] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [178-180] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [184-194] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [198-199] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [208-299] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-108] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [112-114] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [116-117] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [126-129] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [140-158] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [161-163] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [172-299] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-158] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-163] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-167] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-181] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [184-198] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-203] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-243] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-258] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [264-265] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-109] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [112-117] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [128-129] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [132-133] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [144-166] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [169-195] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-121] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [124-133] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [149-166] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [170-171] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [173-195] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [207-208] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [210-214] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [217-219] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [229-232] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [235-237] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [240-241] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [90-100] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [102-107] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [126-130] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '14' starts at frame 133, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [133-133] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-203] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-208] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-20] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [24-109] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [112-117] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [150-158] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [160-163] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [173-194] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [216-217] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [229-236] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [238-243] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [245-249] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [251-254] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [258-299] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-109] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [112-118] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [90-117] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [126-127] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '17' starts at frame 133, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [133-133] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-141] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-158] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-163] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-194] for track '17' has 6 frames without a visible bounding box.
> - Action 'Action_None' range [201-202] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [216-236] for track '17' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [240-241] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [261-262] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-262] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-20] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [24-107] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [112-115] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [15-18] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [90-108] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [112-117] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [126-129] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '20' starts at frame 133, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [133-133] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-158] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-163] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-263] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [268-269] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [19-22] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-109] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [113-118] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [126-164] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [166-170] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [27-30] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [127-133] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [148-152] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [156-157] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [161-163] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [127-130] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [152-153] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [156-157] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [161-163] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [175-181] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [184-188] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [179-181] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [184-188] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [191-194] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [225-226] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [229-241] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [264-271] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [276-290] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [292-296] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [185-186] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [188-194] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [191-193] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [195-196] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [199-202] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [205-207] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [213-217] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [252-254] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [265-271] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [285-289] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [230-232] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [235-236] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [239-299] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [263-264] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [268-270] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [274-290] for track '31' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [292-297] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [269-270] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [272-297] for track '32' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [274-299] for track '33' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [276-293] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [278-290] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [292-297] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [280-299] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [287-290] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [292-297] for track '37' has 1 frames without a visible bounding box.
> - Player track '3' has undefined position. Will map to Position_Unknown.
> - Player track '3' has undefined team_side. Will map to Team_Unknown.
> - Player track '10' has undefined position. Will map to Position_Unknown.
> - Player track '10' has undefined team_side. Will map to Team_Unknown.
> - Player track '11' has undefined position. Will map to Position_Unknown.
> - Player track '11' has undefined team_side. Will map to Team_Unknown.
> - Player track '17' has undefined position. Will map to Position_Unknown.
> - Player track '17' has undefined team_side. Will map to Team_Unknown.
> - Player track '20' has undefined position. Will map to Position_Unknown.
> - Player track '20' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.