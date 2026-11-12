# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `SplitZone_269`
- **Input XML**: `outputs/batch/SplitZone/SplitZone/SplitZone_269/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/SplitZone.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 30 |
| Player Tracks | 30 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 70 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 599 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 599 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Action 'Action_PreSnap' range [14-599] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [490-510] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [14-460] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [14-80] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [14-102] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [104-108] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [451-487] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [504-509] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [511-512] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '8' starts at frame 519, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [519-519] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [451-518] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [14-588] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [14-541] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [546-551] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [14-599] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [14-123] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [128-135] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [141-143] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [148-599] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [14-488] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [494-496] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [14-535] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [539-541] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [553-566] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [14-599] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [14-77] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [451-504] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [507-516] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [519-526] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [519-523] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [526-527] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [84-475] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [486-487] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [512-583] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [587-599] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [540-564] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [578-584] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [590-597] for track '28' has 3 frames without a visible bounding box.
> - Player track '7' has undefined position. Will map to Position_Unknown.
> - Player track '7' has undefined team_side. Will map to Team_Unknown.
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