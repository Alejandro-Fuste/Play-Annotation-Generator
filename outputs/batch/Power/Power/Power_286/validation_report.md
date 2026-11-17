# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_286`
- **Input XML**: `outputs/batch/Power/Power/Power_286/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 28 |
| Player Tracks | 28 |
| Ball Tracks | 0 |
| CSV events parsed | 13 |
| Action Segments inferred | 59 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_DownBlock' range [98-137] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [139-151] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [9-167] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [9-215] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [218-219] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [221-230] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [238-239] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [9-193] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [9-171] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [180-203] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [209-239] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [9-192] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [98-122] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [124-125] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [131-139] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [9-142] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [144-155] for track '8' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [159-162] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [9-119] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [122-147] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [149-239] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [174-231] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [9-116] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [119-122] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [133-134] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [98-173] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [9-99] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [122-131] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [139-150] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [152-153] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [155-156] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [162-216] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [9-239] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [9-123] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [69-182] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [186-188] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [84-97] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [88-239] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [95-239] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [138-239] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [164-165] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [168-175] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [169-205] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [170-221] for track '24' has 2 frames without a visible bounding box.
> - Player track '16' has undefined position. Will map to Position_Unknown.
> - Player track '16' has undefined team_side. Will map to Team_Unknown.
> - Player track '17' has undefined position. Will map to Position_Unknown.
> - Player track '17' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.