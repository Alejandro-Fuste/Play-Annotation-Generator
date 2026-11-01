# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_339`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_339/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 26 |
| Player Tracks | 26 |
| Ball Tracks | 0 |
| CSV events parsed | 24 |
| Action Segments inferred | 70 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '21' (C): higher_priority='Action_BallSnap' [3–14], lower_priority='Action_ZoneBlock' annotated_start=6, effective_Action_ZoneBlock_start=15.
> - Action 'Action_None' range [3-180] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-180] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-32] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-180] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [48-164] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-112] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-153] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-180] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-180] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-180] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [31-48] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-180] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-72] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-37] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [40-180] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-180] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-180] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-180] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [6-21] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [25-27] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [32-33] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-100] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-180] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-136] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-141] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-180] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-178] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-152] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [162-180] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-98] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [102-180] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-139] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-149] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-180] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [36-86] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [45-180] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-180] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-180] for track '25' has 1 frames without a visible bounding box.
> - Player track '22' has undefined position. Will map to Position_Unknown.
> - Player track '22' has undefined team_side. Will map to Team_Unknown.
> - Player track '23' has undefined position. Will map to Position_Unknown.
> - Player track '23' has undefined team_side. Will map to Team_Unknown.
> - Player track '24' has undefined position. Will map to Position_Unknown.
> - Player track '24' has undefined team_side. Will map to Team_Unknown.
> - Player track '25' has undefined position. Will map to Position_Unknown.
> - Player track '25' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.