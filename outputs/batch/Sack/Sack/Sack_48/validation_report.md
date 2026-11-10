# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Sack_48`
- **Input XML**: `outputs/batch/Sack/Sack/Sack_48/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Sack.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 19 |
| Player Tracks | 19 |
| Ball Tracks | 0 |
| CSV events parsed | 9 |
| Action Segments inferred | 35 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [0-132] for track '0' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [138-150] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-129] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [131-132] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-93] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [96-105] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-59] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-93] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [95-97] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [99-100] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [106-107] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [114-140] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-52] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [55-81] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [90-96] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [105-150] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-51] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [55-62] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_SackQuarterback' range [104-150] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-112] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [75-80] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [82-83] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [91-98] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [96-150] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [98-131] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [137-150] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [118-150] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [126-133] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [130-150] for track '18' has 1 frames without a visible bounding box.
> - Player track '12' has undefined position. Will map to Position_Unknown.
> - Player track '12' has undefined team_side. Will map to Team_Unknown.
> - Player track '13' has undefined position. Will map to Position_Unknown.
> - Player track '13' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.