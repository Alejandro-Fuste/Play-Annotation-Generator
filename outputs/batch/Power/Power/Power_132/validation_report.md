# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_132`
- **Input XML**: `outputs/batch/Power/Power/Power_132/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 25 |
| Player Tracks | 25 |
| Ball Tracks | 0 |
| CSV events parsed | 10 |
| Action Segments inferred | 51 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 266: Duplicate assignment for track ID '13' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [3-232] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [3-163] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [165-167] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [173-175] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [3-114] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [3-85] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [87-89] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [3-74] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [79-101] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [104-118] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [124-130] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [134-184] for track '6' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [3-142] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-223] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [3-239] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [3-239] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [3-82] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [54-116] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-153] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-208] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [54-116] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [3-138] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [146-147] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [150-151] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [91-135] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [138-239] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [103-199] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [201-229] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [233-234] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [213-215] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [227-230] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [217-218] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [218-219] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [220-223] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [225-226] for track '24' has 1 frames without a visible bounding box.
> - Player track '3' has undefined position. Will map to Position_Unknown.
> - Player track '3' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.