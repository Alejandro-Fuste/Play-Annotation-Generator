# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Sack_104`
- **Input XML**: `outputs/batch/Sack/Sack/Sack_104/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Sack.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 21 |
| Player Tracks | 21 |
| Ball Tracks | 0 |
| CSV events parsed | 10 |
| Action Segments inferred | 42 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [0-66] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [69-109] for track '0' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-121] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [127-150] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-121] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [132-150] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_WrapQuarterback' range [87-96] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_WrapQuarterback' range [98-101] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-44] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-74] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-130] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [133-137] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [141-150] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-115] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [124-125] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-52] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-71] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [74-150] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-56] for track '11' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [60-150] for track '11' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-51] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [53-70] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [73-75] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [89-146] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-20] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [28-38] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [45-91] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_SackQuarterback' range [114-150] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [42-44] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [47-48] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [50-115] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [121-150] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [57-75] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [58-150] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [59-79] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [86-103] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [124-136] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [127-134] for track '20' has 1 frames without a visible bounding box.
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