# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_21`
- **Input XML**: `outputs/batch/Power/Power/Power_21/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 27 |
| Player Tracks | 27 |
| Ball Tracks | 0 |
| CSV events parsed | 14 |
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
> - Action 'Action_PreSnap' range [22-128] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [134-157] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-210] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-130] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [135-209] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-127] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [145-210] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-210] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-210] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-210] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-210] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [100-106] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [112-131] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [135-167] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [168-181] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [184-187] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-195] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-210] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-210] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [100-164] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-210] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-127] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-210] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-190] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [193-195] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-210] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-210] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [100-131] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-210] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-210] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-176] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [185-208] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-115] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [119-120] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [125-129] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [135-137] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [141-148] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [152-160] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [163-165] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [167-174] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [177-182] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [200-204] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [207-210] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [125-130] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [135-145] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [174-175] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [195-210] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [135-137] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [140-141] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [143-210] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [162-172] for track '24' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [182-183] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [185-186] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [201-210] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [207-209] for track '26' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.