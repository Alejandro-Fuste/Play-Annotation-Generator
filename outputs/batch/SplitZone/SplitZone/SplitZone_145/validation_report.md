# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `SplitZone_145`
- **Input XML**: `outputs/batch/SplitZone/SplitZone/SplitZone_145/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/SplitZone.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 32 |
| Player Tracks | 32 |
| Ball Tracks | 0 |
| CSV events parsed | 21 |
| Action Segments inferred | 91 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 329 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 292: Duplicate assignment for track ID '18' in grid. Overwriting previous assignment.
> - Row 292: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
> - Resolved action overlap for track '21' (C): higher_priority='Action_BallSnap' [118–127], lower_priority='Action_ZoneBlock' annotated_start=121, effective_Action_ZoneBlock_start=128.
> - Action 'Action_None' range [118-308] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-194] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-315] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [118-304] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [308-313] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_SplitBlock' range [119-165] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_SplitBlock' range [170-174] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_SplitBlock' range [199-200] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [210-318] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-207] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-139] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-142] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-148] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-303] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [118-154] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-159] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-176] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-181] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [12-147] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [148-174] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [176-288] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-143] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-146] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-301] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [121-173] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [210-296] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-285] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-303] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-289] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-161] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-168] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [121-140] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [156-198] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [213-216] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [219-223] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [121-152] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-301] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-136] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-208] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [210-298] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-321] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [325-326] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [328-329] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-222] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [224-292] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [118-127] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [145-151] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-173] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-305] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-174] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-289] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [188-285] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [287-295] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [221-223] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [226-258] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [260-265] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [286-294] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [227-288] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [233-290] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [244-246] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [276-285] for track '31' has 3 frames without a visible bounding box.
> - Player track '1' has undefined position. Will map to Position_Unknown.
> - Player track '1' has undefined team_side. Will map to Team_Unknown.
> - Player track '8' has undefined position. Will map to Position_Unknown.
> - Player track '8' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.