# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_335`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_335/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 26 |
| Player Tracks | 26 |
| Ball Tracks | 0 |
| CSV events parsed | 24 |
| Action Segments inferred | 76 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '20' (C): higher_priority='Action_BallSnap' [29–40], lower_priority='Action_ZoneBlock' annotated_start=32, effective_Action_ZoneBlock_start=41.
> - Action 'Action_BlockSecondLevel' range [48-59] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [61-64] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [76-78] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [80-82] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [85-90] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [29-180] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-172] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [29-167] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [76-143] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [145-146] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [29-180] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [29-108] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-169] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [29-180] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [29-138] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-151] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-180] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [29-163] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [29-64] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [67-180] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [29-48] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [50-70] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [72-77] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-96] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [29-78] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-85] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-105] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-180] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [29-180] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [29-180] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [29-180] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [32-110] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-147] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-173] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [32-62] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [29-77] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [29-162] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [41-47] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [63-110] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-162] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [164-180] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-162] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [51-180] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [78-180] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [90-168] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [173-177] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-176] for track '25' has 1 frames without a visible bounding box.
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