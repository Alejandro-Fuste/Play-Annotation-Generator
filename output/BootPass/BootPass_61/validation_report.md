# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: FAILED
- **Video Name**: `BootPass_61`
- **Input XML**: `output/BootPass/BootPass_61/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/BootPass.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 29 |
| Player Tracks | 29 |
| Ball Tracks | 0 |
| CSV events parsed | 7 |
| Action Segments inferred | 67 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 329 |

## **Pipeline Errors**
> [!CAUTION]
> The following critical issues were encountered:
> - Group/position target 'ALL' for action 'Action_PreSnap' at frame 37 could not be resolved to any XML tracks (position/team_side missing).
> - Group/position target 'OL' for action 'Action_RunBlock' at frame 68 could not be resolved to any XML tracks (position/team_side missing).

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Action 'Action_PreSnap' range [37-282] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [37-298] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [302-320] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [37-102] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [107-143] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [146-149] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [156-158] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [162-323] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [37-90] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [37-329] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [37-121] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [37-127] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [130-143] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [145-152] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [154-167] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [213-296] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [298-302] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [37-236] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [37-123] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [128-315] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [37-115] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [117-278] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [283-318] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [37-93] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_FakeHandoff' range [80-97] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-182] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [37-96] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [100-199] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [37-87] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [98-313] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [37-82] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [37-326] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [37-81] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [90-102] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [106-109] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [111-329] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [37-321] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [37-101] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [117-138] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [140-143] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [152-236] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [244-247] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [249-276] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [149-178] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [169-329] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-305] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [307-316] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [274-329] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [312-327] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [314-321] for track '28' has 1 frames without a visible bounding box.
> - Player track '0' has undefined position. Will map to Position_Unknown.
> - Player track '0' has undefined team_side. Will map to Team_Unknown.
> - Player track '1' has undefined position. Will map to Position_Unknown.
> - Player track '1' has undefined team_side. Will map to Team_Unknown.
> - Player track '2' has undefined position. Will map to Position_Unknown.
> - Player track '2' has undefined team_side. Will map to Team_Unknown.
> - Player track '3' has undefined position. Will map to Position_Unknown.
> - Player track '3' has undefined team_side. Will map to Team_Unknown.
> - Player track '4' has undefined position. Will map to Position_Unknown.
> - Player track '4' has undefined team_side. Will map to Team_Unknown.
> - Player track '5' has undefined position. Will map to Position_Unknown.
> - Player track '5' has undefined team_side. Will map to Team_Unknown.
> - Player track '6' has undefined position. Will map to Position_Unknown.
> - Player track '6' has undefined team_side. Will map to Team_Unknown.
> - Player track '7' has undefined position. Will map to Position_Unknown.
> - Player track '7' has undefined team_side. Will map to Team_Unknown.
> - Player track '8' has undefined position. Will map to Position_Unknown.
> - Player track '8' has undefined team_side. Will map to Team_Unknown.
> - Player track '9' has undefined position. Will map to Position_Unknown.
> - Player track '9' has undefined team_side. Will map to Team_Unknown.
> - Player track '10' has undefined position. Will map to Position_Unknown.
> - Player track '10' has undefined team_side. Will map to Team_Unknown.
> - Player track '11' has undefined position. Will map to Position_Unknown.
> - Player track '11' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '25' has undefined position. Will map to Position_Unknown.
> - Player track '25' has undefined team_side. Will map to Team_Unknown.
> - Player track '26' has undefined position. Will map to Position_Unknown.
> - Player track '26' has undefined team_side. Will map to Team_Unknown.
> - Player track '27' has undefined position. Will map to Position_Unknown.
> - Player track '27' has undefined team_side. Will map to Team_Unknown.
> - Player track '28' has undefined position. Will map to Position_Unknown.
> - Player track '28' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Fix the missing/invalid track IDs in the action CSV so they match the XML track structure.
- Resolve the overlapping action segment ranges noted above by adjusting the start frames in the CSV.
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.