# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `SplitZone_221`
- **Input XML**: `outputs/batch/SplitZone/SplitZone/SplitZone_221/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/SplitZone.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 36 |
| Player Tracks | 36 |
| Ball Tracks | 0 |
| CSV events parsed | 20 |
| Action Segments inferred | 135 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 359 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 444: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
> - Validation warning: Action 'Action_ZoneBlock' for track '8' (RT) duration 112 frames exceeds threshold 90 frames [start=130, end=241].
> - Validation warning: Action 'Action_ZoneBlock' for track '18' (LT) duration 112 frames exceeds threshold 90 frames [start=130, end=241].
> - Validation warning: Action 'Action_ZoneBlock' for track '21' (C) duration 112 frames exceeds threshold 90 frames [start=130, end=241].
> - Resolved action overlap for track '21' (C): higher_priority='Action_BallSnap' [127–142], lower_priority='Action_ZoneBlock' annotated_start=130, effective_Action_ZoneBlock_start=143.
> - Action 'Action_None' range [127-181] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [183-225] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [127-220] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-252] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-159] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-166] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-130] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-359] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-359] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [130-148] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [156-174] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [177-180] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [188-211] for track '8' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [249-252] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [283-286] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [294-296] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [302-306] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-234] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [240-244] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [246-359] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [143-146] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-165] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [169-171] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-183] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-195] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [197-199] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [203-219] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-231] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [234-236] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-180] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-188] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [214-218] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [220-222] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-185] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-197] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [203-222] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-226] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [230-231] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [266-269] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [273-274] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [130-152] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [154-155] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-151] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-24] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [30-126] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [130-155] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [162-171] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [175-176] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [180-181] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [183-203] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [206-207] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [212-224] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [242-255] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [286-287] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [297-301] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [305-332] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-19] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-23] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [130-132] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [173-177] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [179-183] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-21] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-132] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-140] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' for track '21' starts at frame 143, but the player has no visible bounding box on this frame.
> - Action 'Action_ZoneBlock' range [143-143] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [148-173] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [242-252] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [258-262] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [72-76] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' for track '23' starts at frame 127, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [127-127] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-131] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-164] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-174] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [176-324] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [328-359] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-210] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [223-228] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [236-254] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [282-283] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [300-301] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [240-242] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [253-254] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [268-269] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [272-276] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [257-259] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [261-268] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [271-276] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [285-288] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [294-295] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [282-294] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [296-359] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [331-332] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [341-359] for track '35' has 1 frames without a visible bounding box.
> - Player track '12' has undefined position. Will map to Position_Unknown.
> - Player track '12' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.