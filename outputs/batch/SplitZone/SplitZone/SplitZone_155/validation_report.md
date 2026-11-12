# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `SplitZone_155`
- **Input XML**: `outputs/batch/SplitZone/SplitZone/SplitZone_155/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/SplitZone.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 30 |
| Player Tracks | 30 |
| Ball Tracks | 0 |
| CSV events parsed | 24 |
| Action Segments inferred | 73 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '14' (C): higher_priority='Action_BallSnap' [89–93], lower_priority='Action_ZoneBlock' annotated_start=92, effective_Action_ZoneBlock_start=94.
> - Action 'Action_None' range [89-104] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-117] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [89-125] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-239] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [89-119] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-88] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-223] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [229-230] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [119-203] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [212-237] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [89-143] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [94-101] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [92-110] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [92-109] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [120-161] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [92-156] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [57-58] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-138] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-128] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [133-134] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-239] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [117-238] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-151] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [154-239] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-181] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-202] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-235] for track '29' has 2 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.