# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OutsideZoneStretch_26`
- **Input XML**: `outputs/batch/OutsideZoneStretch/OutsideZoneStretch/OutsideZoneStretch_26/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OutsideZoneStretch.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 28 |
| Player Tracks | 28 |
| Ball Tracks | 0 |
| CSV events parsed | 14 |
| Action Segments inferred | 64 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 359 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 54: Duplicate assignment for track ID '0' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
> - Action 'Action_PreSnap' range [0-355] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [357-359] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PressEdge' range [147-187] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [222-232] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [237-359] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-254] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [256-313] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-336] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-359] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-216] for track '8' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [219-359] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-269] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [276-316] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-341] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [343-344] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [348-354] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [151-171] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [174-178] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [229-246] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-355] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-359] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-165] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [177-178] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [186-187] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [190-225] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [229-319] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-197] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [200-270] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-202] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [151-168] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [170-171] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [175-228] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [229-283] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-223] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-237] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [16-21] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [29-31] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [35-45] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [47-63] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [71-102] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [105-174] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [179-183] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [188-193] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [195-296] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [168-169] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [178-180] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [184-185] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [221-310] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [248-251] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [319-321] for track '27' has 1 frames without a visible bounding box.
> - Player track '10' has undefined position. Will map to Position_Unknown.
> - Player track '10' has undefined team_side. Will map to Team_Unknown.
> - Player track '18' has undefined position. Will map to Position_Unknown.
> - Player track '18' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.