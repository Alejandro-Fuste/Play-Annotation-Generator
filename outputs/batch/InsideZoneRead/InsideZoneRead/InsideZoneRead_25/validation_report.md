# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_25`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_25/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 28 |
| Player Tracks | 28 |
| Ball Tracks | 0 |
| CSV events parsed | 23 |
| Action Segments inferred | 94 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 52: Duplicate assignment for track ID '15' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Resolved action overlap for track '10' (C): higher_priority='Action_BallSnap' [142–158], lower_priority='Action_ZoneBlock' annotated_start=144, effective_Action_ZoneBlock_start=159.
> - Action 'Action_None' range [142-198] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-264] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [266-267] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-269] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-162] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-181] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-185] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-212] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [220-224] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [226-228] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [235-237] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [239-240] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [251-264] for track '4' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [142-234] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [239-242] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [245-264] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [142-269] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [184-263] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [159-212] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [144-165] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [168-171] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [175-182] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [222-236] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [240-241] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-269] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-269] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-199] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [222-225] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [229-269] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [5-169] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [144-207] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [211-212] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [222-225] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [228-237] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [240-242] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-206] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [5-143] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [144-221] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [222-224] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [228-269] for track '21' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [12-16] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-160] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-178] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [191-211] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [213-244] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [246-256] for track '23' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [260-261] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-199] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-224] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [228-262] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [202-228] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [236-269] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [252-269] for track '26' has 1 frames without a visible bounding box.
> - Player track '4' has undefined position. Will map to Position_Unknown.
> - Player track '4' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.