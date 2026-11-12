# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `SplitZone_222`
- **Input XML**: `outputs/batch/SplitZone/SplitZone/SplitZone_222/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/SplitZone.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 33 |
| Player Tracks | 33 |
| Ball Tracks | 0 |
| CSV events parsed | 18 |
| Action Segments inferred | 84 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 329 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
> - Validation warning: Action 'Action_ZoneBlock' for track '6' (LT) duration 109 frames exceeds threshold 90 frames [start=100, end=208].
> - Validation warning: Action 'Action_ZoneBlock' for track '14' (C) duration 109 frames exceeds threshold 90 frames [start=100, end=208].
> - Resolved action overlap for track '14' (C): higher_priority='Action_BallSnap' [97–111], lower_priority='Action_ZoneBlock' annotated_start=100, effective_Action_ZoneBlock_start=112.
> - Action 'Action_PreSnap' range [22-83] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-301] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-99] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [100-133] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [137-138] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [140-141] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-142] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [145-151] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [132-226] for track '3' has 3 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [231-277] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [280-305] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [100-140] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [97-123] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-137] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [100-154] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_None' for track '6' starts at frame 209, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [209-225] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [227-265] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [100-133] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [97-144] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-203] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-110] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '10' starts at frame 97, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [97-97] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-139] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-31] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [97-149] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [154-164] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-33] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-257] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [279-297] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-156] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [233-244] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [246-250] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [257-259] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [261-265] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [285-294] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [112-120] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [153-154] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [220-267] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [273-280] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [291-297] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-42] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [41-42] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [61-67] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [70-71] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-113] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-123] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-284] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [296-310] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-139] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-149] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-154] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-236] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-205] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [207-259] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [210-329] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [212-284] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [242-266] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [270-301] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [249-270] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [251-300] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [271-295] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [285-291] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [322-324] for track '32' has 1 frames without a visible bounding box.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
> - Player track '16' has undefined position. Will map to Position_Unknown.
> - Player track '16' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.