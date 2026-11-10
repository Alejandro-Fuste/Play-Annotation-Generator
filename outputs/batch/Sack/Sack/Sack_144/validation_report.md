# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Sack_144`
- **Input XML**: `outputs/batch/Sack/Sack/Sack_144/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Sack.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 30 |
| Player Tracks | 30 |
| Ball Tracks | 0 |
| CSV events parsed | 14 |
| Action Segments inferred | 44 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [0-150] for track '0' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-149] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-104] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [106-150] for track '4' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-149] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_SackQuarterback' range [138-150] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-139] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [146-148] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-77] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [80-93] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [111-150] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-121] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [138-150] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-104] for track '14' has 5 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [106-116] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [135-150] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-133] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-68] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [71-123] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-138] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-18] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [43-150] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-78] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [82-90] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [72-76] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [111-112] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [120-124] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [136-137] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [126-142] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [136-140] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [139-150] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [143-144] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [147-150] for track '29' has 1 frames without a visible bounding box.
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