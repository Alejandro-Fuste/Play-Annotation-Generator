# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_188`
- **Input XML**: `outputs/batch/Power/Power/Power_188/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 26 |
| Player Tracks | 24 |
| Ball Tracks | 2 |
| CSV events parsed | 13 |
| Action Segments inferred | 59 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 329 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
> - Action 'Action_PreSnap' range [11-220] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [194-222] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [194-202] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [219-245] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [246-266] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-269] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-297] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-244] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-257] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-212] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [218-259] for track '8' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-225] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [228-231] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-321] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [194-202] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [204-245] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [246-288] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [246-260] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [21-109] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [119-120] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [122-127] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [129-140] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [144-145] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [158-168] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [170-171] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [173-182] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [188-193] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [204-211] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [226-229] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [41-188] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [193-202] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [204-205] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [243-244] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [248-256] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [259-262] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [48-52] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [57-130] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [145-178] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [180-202] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [206-207] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [151-236] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [204-326] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [215-218] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [220-222] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [225-312] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [235-236] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [291-292] for track '24' has 1 frames without a visible bounding box.
> - Player track '16' has undefined position. Will map to Position_Unknown.
> - Player track '16' has undefined team_side. Will map to Team_Unknown.
> - Player track '17' has undefined position. Will map to Position_Unknown.
> - Player track '17' has undefined team_side. Will map to Team_Unknown.
> - Player track '18' has undefined position. Will map to Position_Unknown.
> - Player track '18' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.