# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: FAILED
- **Video Name**: `BootPass_115`
- **Input XML**: `outputs/batch/BootPass/BootPass/BootPass_115/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/BootPass.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 28 |
| Player Tracks | 28 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 62 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
> [!CAUTION]
> The following critical issues were encountered:
> - Row 96, Column 'Run Flat Route': Could not parse frame number from 'Drag' in entry 'Drag,18'.
> - Event 'Action_SecureCatch' at frame 207 targets track ID '39', but it is not found in XML.

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Segment 'Action_RunBlock' for track '3' has invalid range: start=81, end=55. Clamping end to start.
> - Resolved action overlap for track '20' (C): higher_priority='Action_BallSnap' [56–89], lower_priority='Action_RunBlock' annotated_start=81, effective_Action_RunBlock_start=90.
> - Action 'Action_None' range [56-120] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-236] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [56-233] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [238-239] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [56-239] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [56-239] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [56-239] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [56-123] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-127] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-205] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [56-113] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [56-129] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-231] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [56-126] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [81-236] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [81-136] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [90-234] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [56-223] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [114-120] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-239] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [225-230] for track '27' has 2 frames without a visible bounding box.
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
- Fix the missing/invalid track IDs in the action CSV so they match the XML track structure.
- Resolve the overlapping action segment ranges noted above by adjusting the start frames in the CSV.
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.