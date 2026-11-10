# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Sack_149`
- **Input XML**: `outputs/batch/Sack/Sack/Sack_149/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Sack.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 20 |
| Player Tracks | 20 |
| Ball Tracks | 0 |
| CSV events parsed | 9 |
| Action Segments inferred | 48 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [0-210] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-210] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-210] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-155] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [158-210] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-210] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-142] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [144-210] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-15] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-132] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [140-142] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [147-148] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [153-154] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [157-210] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_SackQuarterback' range [181-191] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_SackQuarterback' range [194-195] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_SackQuarterback' range [201-210] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-169] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [183-208] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-210] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-131] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [153-158] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-129] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [131-139] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [142-145] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-153] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [156-157] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [173-210] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [5-7] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [23-25] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [27-32] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [34-37] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [39-40] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [48-65] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [75-81] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [85-87] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [142-143] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [145-148] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [154-155] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [158-159] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [164-210] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [133-139] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [142-210] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [166-175] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [170-180] for track '19' has 1 frames without a visible bounding box.
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