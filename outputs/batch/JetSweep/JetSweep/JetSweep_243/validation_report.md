# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `JetSweep_243`
- **Input XML**: `outputs/batch/JetSweep/JetSweep/JetSweep_243/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/JetSweep.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 31 |
| Player Tracks | 31 |
| Ball Tracks | 0 |
| CSV events parsed | 24 |
| Action Segments inferred | 94 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '21' (C): higher_priority='Action_BallSnap' [22–45], lower_priority='Action_ZoneBlock' annotated_start=33, effective_Action_ZoneBlock_start=46.
> - Action 'Action_None' range [22-239] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [50-217] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [219-239] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [22-142] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-157] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-162] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-175] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-178] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [22-213] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [216-223] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [22-76] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-86] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-90] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [22-118] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [125-161] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [194-196] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-227] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [233-238] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [22-69] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-73] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [22-112] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-117] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-220] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [33-57] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [22-53] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [22-219] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [22-68] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [72-77] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [104-160] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-175] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [50-137] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [33-93] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [98-101] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-155] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [33-88] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [33-48] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [84-88] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [46-81] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [85-91] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [93-103] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-239] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [63-74] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-82] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-239] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-226] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [124-185] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [187-188] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-239] for track '28' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [200-213] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [227-228] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [230-238] for track '29' has 2 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.