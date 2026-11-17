# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_274`
- **Input XML**: `outputs/batch/Power/Power/Power_274/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 30 |
| Player Tracks | 30 |
| Ball Tracks | 0 |
| CSV events parsed | 11 |
| Action Segments inferred | 66 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [0-150] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [152-208] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-117] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [119-164] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [167-183] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [187-239] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-118] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [87-119] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-142] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-200] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-205] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [211-239] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-162] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [87-94] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [104-134] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-151] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-239] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-146] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [149-153] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-27] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [47-48] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [109-112] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [119-138] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [142-145] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [150-218] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-129] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [131-132] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-128] for track '12' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-116] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [133-146] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-83] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [97-98] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [102-136] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [138-141] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [110-192] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [122-147] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [149-150] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [152-160] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [164-165] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [171-172] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [123-220] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [230-231] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [147-178] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [154-159] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [204-239] for track '25' has 2 frames without a visible bounding box.
> - Player track '6' has undefined position. Will map to Position_Unknown.
> - Player track '6' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '28' has undefined position. Will map to Position_Unknown.
> - Player track '28' has undefined team_side. Will map to Team_Unknown.
> - Player track '29' has undefined position. Will map to Position_Unknown.
> - Player track '29' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.