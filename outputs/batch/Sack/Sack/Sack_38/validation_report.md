# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Sack_38`
- **Input XML**: `outputs/batch/Sack/Sack/Sack_38/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Sack.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 21 |
| Player Tracks | 20 |
| Ball Tracks | 1 |
| CSV events parsed | 9 |
| Action Segments inferred | 33 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [0-143] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [145-180] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-160] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [162-180] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-162] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [167-178] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-124] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [133-136] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [138-179] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-108] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-1] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_SackQuarterback' range [169-180] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [104-180] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [112-178] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [123-180] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [126-158] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [130-134] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [158-159] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [133-142] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [144-147] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [165-166] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [168-180] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [169-179] for track '20' has 2 frames without a visible bounding box.
> - Player track '3' has undefined position. Will map to Position_Unknown.
> - Player track '3' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '20' has undefined position. Will map to Position_Unknown.
> - Player track '20' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.