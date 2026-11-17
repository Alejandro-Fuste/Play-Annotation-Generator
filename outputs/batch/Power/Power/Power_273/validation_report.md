# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_273`
- **Input XML**: `outputs/batch/Power/Power/Power_273/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 26 |
| Player Tracks | 26 |
| Ball Tracks | 0 |
| CSV events parsed | 12 |
| Action Segments inferred | 54 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 546: Duplicate assignment for track ID '3' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [25-165] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [25-160] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [162-163] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [172-181] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [115-155] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-239] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [25-235] for track '9' has 7 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [25-171] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [178-183] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [185-190] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [192-193] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [25-156] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [162-189] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [192-239] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [25-142] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [147-187] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [25-153] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [156-167] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [170-239] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [25-116] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [118-119] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [25-136] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [139-180] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [182-217] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [220-221] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [25-105] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [69-107] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [112-114] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [117-127] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [129-150] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [154-191] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [201-239] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [151-170] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [172-239] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [173-174] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [217-218] for track '25' has 1 frames without a visible bounding box.
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