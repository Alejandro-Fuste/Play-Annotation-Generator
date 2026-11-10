# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Sack_102`
- **Input XML**: `outputs/batch/Sack/Sack/Sack_102/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Sack.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 23 |
| Player Tracks | 23 |
| Ball Tracks | 0 |
| CSV events parsed | 11 |
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
> - Action 'Action_PreSnap' range [0-180] for track '0' has 6 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-65] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [67-101] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_SackQuarterback' range [138-154] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-98] for track '3' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-138] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-104] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [107-180] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-78] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [80-95] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-132] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-156] for track '8' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [158-180] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-137] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [139-142] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-80] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [82-83] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [87-89] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-81] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [84-87] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-87] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [90-91] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [93-180] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-60] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [65-80] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [91-180] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-78] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [76-180] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [95-149] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [153-155] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [158-176] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [98-180] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [103-180] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [117-146] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [148-180] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [125-178] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [147-170] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [168-180] for track '22' has 2 frames without a visible bounding box.
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
> - Player track '21' has undefined position. Will map to Position_Unknown.
> - Player track '21' has undefined team_side. Will map to Team_Unknown.
> - Player track '22' has undefined position. Will map to Position_Unknown.
> - Player track '22' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.