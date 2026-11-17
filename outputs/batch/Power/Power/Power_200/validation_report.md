# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_200`
- **Input XML**: `outputs/batch/Power/Power/Power_200/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 25 |
| Player Tracks | 25 |
| Ball Tracks | 0 |
| CSV events parsed | 11 |
| Action Segments inferred | 67 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Track ID '18' in Player Track ID sheet does not exist in MOT gt.txt.
> - Track ID '19' in Player Track ID sheet does not exist in MOT gt.txt.
> - Track ID '21' in Player Track ID sheet does not exist in MOT gt.txt.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [0-33] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-144] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [158-159] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [165-189] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [193-194] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [199-202] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-152] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [155-239] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-208] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-239] for track '4' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-134] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-221] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [224-230] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [236-237] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-212] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [54-63] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [65-98] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-134] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-80] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [82-158] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [161-163] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [165-210] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [219-220] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [224-239] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-128] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-71] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [84-88] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [109-118] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-101] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [109-192] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [200-239] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-117] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-60] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [102-153] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [159-163] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [165-183] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [185-207] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [213-239] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-81] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [85-131] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [136-159] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [161-233] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-92] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [94-112] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [54-63] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [65-70] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [77-92] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [98-113] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-115] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [122-138] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [148-189] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [176-221] for track '21' has 1 frames without a visible bounding box.
> - Player track '0' has undefined position. Will map to Position_Unknown.
> - Player track '0' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.