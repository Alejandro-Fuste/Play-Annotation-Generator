# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Sack_209`
- **Input XML**: `outputs/batch/Sack/Sack/Sack_209/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Sack.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 20 |
| Player Tracks | 20 |
| Ball Tracks | 0 |
| CSV events parsed | 9 |
| Action Segments inferred | 36 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [0-180] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-146] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [149-180] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-58] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [60-169] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-143] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [146-180] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-111] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-151] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [154-158] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [160-180] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-174] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_SackQuarterback' range [169-180] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-70] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [76-125] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [127-128] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-2] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [4-180] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [9-25] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [27-51] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [99-105] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [107-111] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [40-41] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [45-46] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [124-179] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [143-180] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [145-149] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [158-159] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [161-166] for track '19' has 2 frames without a visible bounding box.
> - Player track '2' has undefined position. Will map to Position_Unknown.
> - Player track '2' has undefined team_side. Will map to Team_Unknown.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
> - Player track '16' has undefined position. Will map to Position_Unknown.
> - Player track '16' has undefined team_side. Will map to Team_Unknown.
> - Player track '17' has undefined position. Will map to Position_Unknown.
> - Player track '17' has undefined team_side. Will map to Team_Unknown.
> - Player track '18' has undefined position. Will map to Position_Unknown.
> - Player track '18' has undefined team_side. Will map to Team_Unknown.
> - Player track '19' has undefined position. Will map to Position_Unknown.
> - Player track '19' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.