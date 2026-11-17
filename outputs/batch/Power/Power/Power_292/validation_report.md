# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_292`
- **Input XML**: `outputs/batch/Power/Power/Power_292/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 30 |
| Player Tracks | 30 |
| Ball Tracks | 0 |
| CSV events parsed | 14 |
| Action Segments inferred | 69 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 584: Duplicate assignment for track ID '4' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [12-91] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [93-239] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-116] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [12-93] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [12-97] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [103-109] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [114-201] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [12-239] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [12-89] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [91-239] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [12-184] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [12-114] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [12-193] for track '8' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [196-203] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [60-100] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' for track '9' starts at frame 107, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [107-107] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-111] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-124] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-131] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [12-87] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [12-98] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [102-111] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [114-239] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [12-151] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [12-99] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [102-142] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [12-90] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-239] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [60-67] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [70-97] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-110] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-152] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [12-60] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [108-110] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [116-239] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [12-84] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [89-99] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [114-128] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [130-239] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [12-56] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [65-74] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [77-94] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [96-97] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [100-239] for track '19' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-14] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [93-235] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [119-142] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [144-150] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [152-170] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [128-134] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [157-158] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [201-206] for track '28' has 1 frames without a visible bounding box.
> - Player track '6' has undefined position. Will map to Position_Unknown.
> - Player track '6' has undefined team_side. Will map to Team_Unknown.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
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